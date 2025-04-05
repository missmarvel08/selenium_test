const { Builder, By, until } = require('selenium-webdriver');
const { waitForElementVisible } = require('./utils/helper');

(async function loginTest() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        await driver.get('http://your-login-page-url.com');

        // Wait for the username field to be visible and input username
        await waitForElementVisible(driver, By.name('username'));
        await driver.findElement(By.name('username')).sendKeys('your-username');

        // Wait for the password field to be visible and input password
        await waitForElementVisible(driver, By.name('password'));
        await driver.findElement(By.name('password')).sendKeys('your-password');

        // Click the login button
        await driver.findElement(By.id('login-button')).click();

        // Wait for the login to complete and verify successful login
        await driver.wait(until.urlIs('http://your-expected-url-after-login.com'), 5000);
        console.log('Login test passed!');
    } catch (error) {
        console.error('Login test failed:', error);
    } finally {
        await driver.quit();
    }
})();