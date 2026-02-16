# Merge Conflict Documentation

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



