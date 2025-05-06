# Test Case: Blank Fields – test-case-blank-fields-04

## Title
Verify error message or behavior when login form is submitted with blank fields

## Test ID
test-case-blank-fields-04

## Priority
Medium

## Preconditions
- User is on the login page.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Chrome, Firefox
- **OS**: Windows/Linux/macOS

## Steps
1. Open the login page.
2. Leave both the **Username** and **Password** fields empty.
3. Click **Submit**

## Expected Result
- Login attempt is rejected.
- An error message is displayed such as _“Username and Password cannot be blank”_ or similar.
- User remains on login page.

## Postconditions
- No session is created.

## Pass/Fail Criteria
- **Pass**: Login fails and appropriate error message is shown.
- **Fail**: Login proceeds or no error feedback is given.
