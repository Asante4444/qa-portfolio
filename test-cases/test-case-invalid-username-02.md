# Test Case: Invalid Username – test-case-invalid-username-02

## Title
Verify error message when logging in with an invalid username

## Test ID
test-case-invalid-username-02

## Priority
High

## Preconditions
- User is on the login page.
- Valid password is known.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Chrome, Firefox
- **OS**: Windows/Linux/macOS

## Steps
1. Open the login page.
2. Enter invalid username: `wrongUser`
3. Enter valid password: `Password123`
4. Click **Submit**

## Expected Result
- Login fails.
- Error message: _“Your username is invalid!”_ is displayed.
- User remains on login page.

## Postconditions
- No session is created.

## Pass/Fail Criteria
- **Pass**: Error appears and login is denied.
- **Fail**: No error appears or user is logged in unexpectedly.
