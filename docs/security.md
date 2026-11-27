
# Security Guidelines

## 1. Secret Management

- Never commit API keys, passwords, or private credentials.
- Keep real environment variables in `.env`.
- Use a strong, randomly generated Flask secret key.
- Rotate exposed credentials immediately.

## 2. File Upload Security

Uploaded satellite imagery must be validated before processing.

Recommended protections:

- Restrict permitted file formats.
- Validate file contents, not only extensions.
- Enforce upload size limits.
- Generate server-side filenames.
- Reject malformed or corrupted files.
- Prevent path traversal attacks.

## 3. Uploaded Data Protection

Satellite imagery may contain sensitive geographic information.

- Restrict access to uploaded files.
- Avoid publicly exposing private imagery.
- Define file retention and deletion policies.
- Do not upload confidential datasets to public repositories.

## 4. Application Deployment

For production:

- Disable Flask debug mode.
- Use a production WSGI server.
- Enable HTTPS.
- Configure secure HTTP headers.
- Apply authentication and authorization.
- Keep dependencies updated.
- Monitor application logs.

## 5. Model Security

- Use trusted model checkpoints.
- Verify model file sources.
- Avoid loading untrusted serialized model files.
- Restrict access to model storage.

## 6. Dependency Security

Review dependencies regularly and update vulnerable packages.

## 7. Responsible Use

Use satellite analysis outputs responsibly. Verify important findings independently before making operational decisions.

## Reporting a Security Issue

Do not publish sensitive vulnerability details or private data in public issues. Contact the repository maintainer through an appropriate private channel.
