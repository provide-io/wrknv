# TODO.md - wrkenv Development Tasks

## High Priority

### Testing & Quality
- [ ] **Improve Test Coverage** - Currently at 44%, critical functionality untested
  - Download/Install operations have only 11-14% coverage
  - Tool managers have 18-24% coverage
  - Container module has 0% coverage

### Core Functionality
- [ ] **Better Error Handling** - UV installation failures in containers need graceful recovery
- [ ] **Fix Sibling Installation Logic** - The `test_simple_string_siblings` test is failing because the template was changed to always use `--force-reinstall --no-deps` for simple strings. This needs to be fixed to respect the `with_deps` default while still handling Python version conflicts gracefully.

## Medium Priority

### Features
- [ ] **Profile-Based Matrix Testing** - Use named profiles instead of version combinations
- [ ] **Implement Real Package Publish** - Currently returns mock data
- [ ] **Test Container Functionality** - Verify Docker integration works

### Integration
- [ ] **Remove Package Commands from tofusoup** - Eliminate duplication
- [ ] **Update Documentation** - Update README with new features

## Low Priority

### Future Considerations
- [ ] **Container Module Review** - Consider removing if unused (0% coverage)
- [ ] **Generic Tool Management vs Ecosystem Focus** - Decide on scope
- [ ] **UV Installation in Restricted Environments** - Handle failures gracefully
- [ ] **`bfiles` Integration** - Integrate the `bfiles` utility for bundling files.
- [ ] **Bundler System** - Implement a generic, extensible framework for managing directory-based bundles.

## Completed
- [x] Extract workenv from tofusoup
- [x] Create standalone wrkenv package
- [x] Implement core CLI functionality
- [x] Add container management system
- [x] Add visual UX enhancements
- [x] Shell integration & aliases
- [x] Package management commands
- [x] Dynamic sibling configuration (2025-08-11)
- [x] Unified Siblings Format (2025-08-11)
- [x] Python Version Mismatch Detection (2025-08-11)
