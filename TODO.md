# TODO.md - wrkenv Development Tasks

## High Priority

### Testing & Quality
- [ ] **Improve Test Coverage** - Currently at 34%, critical functionality untested
  - Download/Install operations have only 11-14% coverage
  - Tool managers have 18-24% coverage
  - Container module has 0% coverage

### Core Functionality
- [x] **Dynamic Sibling Configuration** - ✅ COMPLETED - Read sibling patterns from wrkenv.toml
- [ ] **Better Error Handling** - UV installation failures in containers need graceful recovery

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

## Completed
- [x] Extract workenv from tofusoup
- [x] Create standalone wrkenv package
- [x] Implement core CLI functionality
- [x] Add container management system
- [x] Add visual UX enhancements
- [x] Shell integration & aliases
- [x] Package management commands
- [x] Dynamic sibling configuration (2025-08-11)