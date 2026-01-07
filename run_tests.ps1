# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Run tests
pytest

# Exit with pytest exit code
exit $LASTEXITCODE
