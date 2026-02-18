# Merge Conflict Documentation

## Conflict Scenario

Both Developer A and Developer B modified README.md simultaneously
in separate feature branches.

When merging feature/ner-endpoint into main,
a merge conflict occurred.

## Conflict Location

README.md – Setup Instructions section

## Resolution Process

1. Git showed conflict markers (<<<<, ====, >>>>)
2. We manually combined both changes.
3. Removed conflict markers.
4. Committed resolution with message:
   "Resolved merge conflict in README"

## Learning

- Understood how Git identifies conflicting line edits
- Practiced manual conflict resolution
