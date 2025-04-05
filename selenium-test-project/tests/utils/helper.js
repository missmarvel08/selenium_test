module.exports = {
    waitForElementToBeVisible: async function(driver, element, timeout = 5000) {
        const { until } = require('selenium-webdriver');
        await driver.wait(until.elementIsVisible(element), timeout);
    },
    
    clickElement: async function(driver, element) {
        await this.waitForElementToBeVisible(driver, element);
        await element.click();
    },

    inputText: async function(driver, element, text) {
        await this.waitForElementToBeVisible(driver, element);
        await element.clear();
        await element.sendKeys(text);
    }
};