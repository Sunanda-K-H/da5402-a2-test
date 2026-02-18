# Merge Conflict Documentation

<<<<<<< HEAD
## Summary

A merge conflict occurred while merging the `feature/ner-endpoint` branch into `main`.

## Files Involved

The conflict occurred in the following files:

- `.gitignore`
- `app/main.py`
- `requirements.txt`

## Cause of Conflict

The conflict happened because both branches modified overlapping sections of the same files independently.

- The `feature/ner-endpoint` branch added NER-related imports and router configurations.
- The `main` branch already contained router imports for translation and image generation.
- Both branches also modified `.gitignore` and `requirements.txt` independently.

When the first branch was merged, the second branch became outdated relative to `main`. Git was unable to automatically determine which changes to keep, resulting in a merge conflict.

## Conflict Resolution

The conflict was resolved manually by:

- Combining entries in `.gitignore` to preserve all necessary ignore rules.
- Merging dependencies in `requirements.txt` while removing duplicates.
- Updating `app/main.py` to include all routers (translation, image generation, NER, and speech) in a single consistent FastAPI application setup.
- Removing all Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) after resolving differences.

After resolving the conflicts, the changes were committed and the pull request was successfully merged.

## Final Outcome

The application runs successfully with all four endpoints:
- Translation
- Image Generation
- NER
- Speech Synthesis



=======
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
>>>>>>> feature/ner-endpoint
