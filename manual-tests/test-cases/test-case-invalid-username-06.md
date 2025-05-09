# Test Case: Invalid Username – test-case-invalid-username-06

## Title
Verify error message when logging in with an incorrect username

## Test ID
test-case-invalid-username-06

## Priority
High

## Preconditions
- User is on the login page.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Chrome, Firefox
- **OS**: Windows/Linux/macOS

## Steps
1. Open the login page.
2. Enter an invalid username (e.g., `wrongUser`)
3. Enter valid password: `Password123`
4. Click **Submit**

## Expected Result
- Login attempt fails.
- Error message is displayed: _“Your username is invalid!”_
- User remains on login page.

## Postconditions
- No session is created.

## Pass/Fail Criteria
- **Pass**: Login fails and proper error is displayed.
- **Fail**: Login succeeds or error is not shown when using an invalid username.
