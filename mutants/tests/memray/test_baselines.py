#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for memray.baselines module."""

from __future__ import annotations

import json
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.memray.baselines import (
    DEFAULT_ALLOCATION_THRESHOLD,
    assert_allocation_within_threshold,
    load_baselines,
    parse_peak_memory,
    parse_total_allocations,
    parse_total_memory,
    update_baseline,
)


class TestLoadBaselines(FoundationTestCase):
    """Tests for load_baselines."""

    def test_returns_empty_dict_when_file_missing(self) -> None:
        tmp = self.create_temp_dir()
        result = load_baselines(tmp / "baselines.json")
        assert result == {}

    def test_returns_data_from_existing_file(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        path.write_text('{"my_test": 100}')
        result = load_baselines(path)
        assert result == {"my_test": 100}

    def test_returns_dict_type(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        path.write_text('{"a": 1, "b": 2}')
        result = load_baselines(path)
        assert isinstance(result, dict)


class TestUpdateBaseline(FoundationTestCase):
    """Tests for update_baseline."""

    def test_creates_file_when_missing(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        update_baseline(path, "my_key", 42)
        assert path.exists()

    def test_writes_key_value(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        update_baseline(path, "my_key", 42)
        data = json.loads(path.read_text())
        assert data["my_key"] == 42

    def test_appends_to_existing_file(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        path.write_text('{"existing": 10}\n')
        update_baseline(path, "new_key", 99)
        data = json.loads(path.read_text())
        assert data["existing"] == 10
        assert data["new_key"] == 99

    def test_overwrites_existing_key(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        path.write_text('{"my_key": 10}\n')
        update_baseline(path, "my_key", 999)
        data = json.loads(path.read_text())
        assert data["my_key"] == 999

    def test_file_ends_with_newline(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        update_baseline(path, "k", 1)
        assert path.read_text().endswith("\n")

    def test_keys_are_sorted(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        update_baseline(path, "z_key", 1)
        update_baseline(path, "a_key", 2)
        data = json.loads(path.read_text())
        assert list(data.keys()) == sorted(data.keys())


class TestAssertAllocationWithinThreshold(FoundationTestCase):
    """Tests for assert_allocation_within_threshold."""

    def test_skips_on_first_run_and_records_baseline(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        with pytest.raises(pytest.skip.Exception):
            assert_allocation_within_threshold("new_key", 100, {}, path)
        data = json.loads(path.read_text())
        assert data["new_key"] == 100

    def test_passes_when_within_threshold(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        baselines = {"my_test": 100}
        # 110 is 10% above 100, within default 15% threshold
        assert_allocation_within_threshold("my_test", 110, baselines, path)

    def test_fails_when_above_threshold(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        baselines = {"my_test": 100}
        with pytest.raises(AssertionError, match="Allocation regression"):
            assert_allocation_within_threshold("my_test", 200, baselines, path)

    def test_passes_when_at_threshold(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        baselines = {"my_test": 100}
        # int(100 * 1.15) = 114 due to floating point; 114 should pass
        assert_allocation_within_threshold("my_test", 114, baselines, path)

    def test_updates_baseline_when_env_var_set(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        baselines = {"my_test": 100}
        with mock.patch.dict("os.environ", {"MEMRAY_UPDATE_BASELINE": "1"}):
            assert_allocation_within_threshold("my_test", 200, baselines, path)
        data = json.loads(path.read_text())
        assert data["my_test"] == 200

    def test_custom_threshold(self) -> None:
        tmp = self.create_temp_dir()
        path = tmp / "baselines.json"
        baselines = {"my_test": 100}
        # 5% threshold: 106 should fail
        with pytest.raises(AssertionError):
            assert_allocation_within_threshold("my_test", 106, baselines, path, threshold=0.05)

    def test_default_threshold_constant(self) -> None:
        assert DEFAULT_ALLOCATION_THRESHOLD == 0.15


class TestParseTotalAllocations(FoundationTestCase):
    """Tests for parse_total_allocations."""

    def test_parses_standard_format(self) -> None:
        output = "Total allocations:\n    3878431\n"
        assert parse_total_allocations(output) == 3878431

    def test_parses_with_commas(self) -> None:
        output = "Total allocations:\n    3,878,431\n"
        assert parse_total_allocations(output) == 3878431

    def test_returns_zero_when_not_found(self) -> None:
        assert parse_total_allocations("no match here") == 0

    def test_case_insensitive(self) -> None:
        output = "TOTAL ALLOCATIONS:\n    500\n"
        assert parse_total_allocations(output) == 500

    def test_returns_zero_on_empty_string(self) -> None:
        assert parse_total_allocations("") == 0

    def test_ignores_non_matching_lines(self) -> None:
        output = "Peak memory:\n    44.394MB\nTotal allocations:\n    42\n"
        assert parse_total_allocations(output) == 42

    def test_total_allocations_label_with_no_numeric_next_line(self) -> None:
        """Line 112->109: 'total allocations' found but next line has no digits → loop continues."""
        output = "Total allocations:\n(unavailable)\n"
        assert parse_total_allocations(output) == 0


class TestParsePeakMemory(FoundationTestCase):
    """Tests for parse_peak_memory."""

    def test_parses_standard_format(self) -> None:
        output = "Peak memory:\n    44.394MB\n"
        assert parse_peak_memory(output) == "44.394MB"

    def test_returns_empty_when_not_found(self) -> None:
        assert parse_peak_memory("no match here") == ""

    def test_case_insensitive(self) -> None:
        output = "PEAK MEMORY:\n    100MB\n"
        assert parse_peak_memory(output) == "100MB"

    def test_returns_empty_on_empty_string(self) -> None:
        assert parse_peak_memory("") == ""

    def test_strips_whitespace(self) -> None:
        output = "Peak memory:\n      1.5GB   \n"
        assert parse_peak_memory(output) == "1.5GB"


class TestParseTotalMemory(FoundationTestCase):
    """Tests for parse_total_memory."""

    def test_parses_standard_format(self) -> None:
        output = "Total memory allocated:\n    569.040MB\n"
        assert parse_total_memory(output) == "569.040MB"

    def test_returns_empty_when_not_found(self) -> None:
        assert parse_total_memory("no match here") == ""

    def test_case_insensitive(self) -> None:
        output = "TOTAL MEMORY ALLOCATED:\n    200MB\n"
        assert parse_total_memory(output) == "200MB"

    def test_returns_empty_on_empty_string(self) -> None:
        assert parse_total_memory("") == ""

    def test_strips_whitespace(self) -> None:
        output = "Total memory allocated:\n      2.0GB   \n"
        assert parse_total_memory(output) == "2.0GB"


# 🧰🌍🔚
