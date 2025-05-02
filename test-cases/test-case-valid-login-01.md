# Test Case: Valid Login – test-case-valid-login-01

## Title
Verify successful login with valid credentials

## Test ID
test-case-valid-login-01

## Test Priority
High

## Preconditions
- User has access to the login page.
- Browser cache and cookies cleared to avoid session artifacts.

## Test Environment
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Browser**: Latest stable versions of Chrome, Firefox, and Edge
- **OS**: Windows/macOS/Linux

## Steps to Execute
1. Open a browser and go to: https://practicetestautomation.com/practice-test-login/
2. Locate the **Username** input field and enter: `student`
3. Locate the **Password** input field and enter: `Password123`
4. Click the **Submit** button.
5. Wait for the response and observe the resulting page.

## Expected Result
- User is redirected to a secure area at `https://practicetestautomation.com/logged-in-successfully/`
- Page contains confirmation text: _"Logged In Successfully"_
- A **Log out** button is visible
- No error messages should appear

## Postconditions
- Session remains active until the user logs out or the browser is closed.

## Pass/Fail Criteria
- **Pass**: All expected results are met without exceptions.
- **Fail**: If login does not succeed, error message is shown incorrectly, or redirection fails.

## Test Data
| Field     | Value        |
|-----------|--------------|
| Username  | student      |
| Password  | Password123  |

## Notes
- This test should be automated for future regression runs.
- Ensure to include wait conditions for redirection and page load.
