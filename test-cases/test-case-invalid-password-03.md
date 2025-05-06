# Test Case: Invalid Password – test-case-invalid-password-03

## Title
Verify error message when logging in with an incorrect password

## Test ID
test-case-invalid-password-03

## Priority
High

## Preconditions
- User is on the login page.
- Valid username is known.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Chrome, Firefox
- **OS**: Windows/Linux/macOS

## Steps
1. Open the login page.
2. Enter valid username: `student`
3. Enter invalid password: `wrongPass123`
4. Click **Submit**

## Expected Result
- Login fails.
- Error message: _“Your password is invalid!”_ is displayed.
- User remains on login page.

## Postconditions
- No session is created.

## Pass/Fail Criteria
- **Pass**: Error message appears and access is denied.
- **Fail**: Login proceeds or no error message appears.
