'use strict';

function createLogger(loggerFunction, InnerDate) {
  loggerFunction =
    loggerFunction || console.log;
  InnerDate = InnerDate || Date;
  function logInfo(message) {
    var date = new InnerDate();
    var logMessage = 'INFO ' +
      message +
      ' ' +
      date.toISOString();
    loggerFunction(logMessage);
  }

  return {
    logInfo: logInfo
  };
}

module.exports = createLogger;
