const {Builder,By} = require('selenium-webdriver');
(
  async function (){
    let arr = [[1,2,3],[4,5,9],[2,3,5],[1,1,2]];
    for(it of arr){
      const driver  = new Builder().forBrowser('chrome').build();
      // await driver.get("file://"+__dirname+"/index.html");
      await driver.get("http://localhost:8010/");

      await driver.findElement(By.id('num1')).sendKeys(it[0].toString());
      await driver.findElement(By.id('num2')).sendKeys(it[1].toString());
      await driver.findElement(By.id('btn')).click();

      await driver.sleep(1000);

      let res = await driver.findElement(By.id('res')).getAttribute('value');
      if(res == it[2]){
        console.log("Automation test is Sucessful result : ",res);
      }else{
        console.error('failed');
      }
      await driver.quit();
    }
  }
)();