# Bug Report 01

## Title
"Username or password is incorrect" message is not dismissed after correcting login credentials

## Environment
- **Browser**: Chrome v123.0.6312.86
- **OS**: Windows 10
- **Device**: Desktop
- **URL**: https://practicetestautomation.com/practice-test-login/
- **Date Reported**: 2025-05-01

## Precondition
User previously attempted to log in with incorrect credentials and received an error message.

## Steps to Reproduce
1. Navigate to: https://practicetestautomation.com/practice-test-login/
2. Enter incorrect credentials:
   - Username: `incorrectUser`
   - Password: `wrongPassword`
3. Click the **Submit** button.
4. Observe the error message: _"Your username is invalid!"_ or _"Your password is invalid!"_
5. Without refreshing the page, update the credentials to:
   - Username: `student`
   - Password: `Password123`
6. Click **Submit** again.

## Expected Result
- Upon successful login, the error message should disappear.
- User should be redirected to the secure area page confirming successful login.

## Actual Result
- Login succeeds (user is redirected), but the previous error message remains visible for a short time before the page changes.
- This may confuse the user about whether the login actually worked.

## Severity
Low – cosmetic/UI inconsistency; does not prevent login but may impact user experience.

## Suggested Fix
Ensure that error messages are programmatically cleared on new login attempts or upon successful login redirect.

## Attachments
- Screenshot of lingering error message before redirect.
- Browser console logs (if applicable).
