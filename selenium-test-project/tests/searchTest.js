const { Builder, By, until } = require('selenium-webdriver');
const { waitForElement } = require('./utils/helper');

(async function searchTest() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        await driver.get('http://yourwebsite.com/search'); // Replace with your search page URL

        // Perform a search
        await waitForElement(driver, By.name('searchBox')); // Adjust selector as needed
        await driver.findElement(By.name('searchBox')).sendKeys('test search query'); // Replace with your search query
        await driver.findElement(By.id('searchButton')).click(); // Adjust selector as needed

        // Verify search results
        await driver.wait(until.titleContains('test search query'), 5000); // Adjust condition as needed
        const results = await driver.findElements(By.css('.search-result')); // Adjust selector as needed
        if (results.length > 0) {
            console.log('Search test passed: Results found.');
        } else {
            console.log('Search test failed: No results found.');
        }
    } catch (error) {
        console.error('Error during search test:', error);
    } finally {
        await driver.quit();
    }
})();