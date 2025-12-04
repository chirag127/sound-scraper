# Security Policy

## Reporting a Vulnerability

At Apex, we take the security of our projects extremely seriously. If you discover any security vulnerabilities within this project, please report them promptly to us through the appropriate channels.

## Vulnerability Disclosure Policy

We follow a responsible disclosure process. We ask that you do not disclose vulnerabilities publicly until we have had a reasonable time to address them. We will acknowledge receipt of your report within **48 hours** and will provide an update on the status of the fix within **7 days**.

## Supported Versions

Currently, all actively developed versions of this project are considered to be supported with security updates.

## Process for Handling Security Vulnerabilities

1.  **Report:** Security issues should be reported via email to `security@example.com` (replace with actual security contact if available) or preferably by creating a **private vulnerability report** if your platform supports it (e.g., GitHub's security advisory feature).
2.  **Triage:** The security team will triage the report and acknowledge receipt within **48 hours**.
3.  **Fix:** A fix will be developed and tested. We aim to provide a patch within **7 days** of the report, depending on the complexity.
4.  **Disclose:** Once a fix is available, we will coordinate with the reporter for public disclosure. This typically involves releasing a new version and updating relevant documentation, including the `README.md` and `AGENTS.md` files.
5.  **Communicate:** We will communicate the status and resolution through GitHub issues and release notes.

## Security Best Practices for Developers

As a developer contributing to this project, you are expected to adhere to the following security best practices:

*   **Code Quality:** Write clean, maintainable, and secure code. Follow the principles of SOLID, DRY, and YAGNI.
*   **Dependency Management:** Ensure all dependencies are up-to-date and from trusted sources. Use `uv` for dependency management and regularly scan for vulnerabilities.
*   **Input Validation:** Sanitize and validate all external inputs to prevent injection attacks (e.g., SQL injection, command injection).
*   **Error Handling:** Implement robust error handling that does not leak sensitive information.
*   **Secrets Management:** Never hardcode secrets (API keys, passwords, etc.) directly in the code. Use environment variables or a secure secrets management system.
*   **Testing:** Write comprehensive tests, including security-focused tests where applicable, using Pytest.
*   **Linting & Formatting:** Ensure all code passes linting and formatting checks by Ruff.

## Contact

For any security-related questions or concerns, please reach out to the security team at `security@example.com`.