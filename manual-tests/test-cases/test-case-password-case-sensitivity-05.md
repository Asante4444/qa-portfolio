# Test Case: Password Case Sensitivity – test-case-password-case-sensitivity-05

## Title
Verify that the password field is case-sensitive

## Test ID
test-case-password-case-sensitivity-05

## Priority
Medium

## Preconditions
- User is on the login page.
- Valid credentials are known.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Chrome, Firefox
- **OS**: Windows/Linux/macOS

## Steps
1. Open the login page.
2. Enter valid username: `student`
3. Enter password in incorrect case (e.g., `password123` instead of `Password123`)
4. Click **Submit**

## Expected Result
- Login fails.
- Error message appears: _“Your password is invalid!”_
- User remains on login page.

## Postconditions
- No session is created.

## Pass/Fail Criteria
- **Pass**: Error is shown and access is denied due to incorrect casing.
- **Fail**: Login proceeds or no error is displayed despite incorrect password case.
