# FastFind – Rapidly search for answers without leaving the command line.

## Introduction
FastFind is a command-line tool designed to help you with everyday tasks right from your terminal, so you can stay focused without needing to switch over to a browser. Whether you're checking stock prices or finding out when the next bank holiday is, FastFind makes it easy to perform simple searches that we all do daily without the distraction of opening a browser.

This project is meant to grow over time with more functionalities, and everyone is welcome to contribute to make FastFind smarter!

## Features
Currently, FastFind supports the following functionalities:
1. Stock Price Lookup: <br>You can get the latest price for any stock by providing the stock symbol.<br>
    Example:
    ```ff --stock AAPL # prints the value of the apple stock```
2. Bank Holiday Check:
FastFind can tell you when is the next UK bank holiday.
Example:
    ```
    ff --bank-holiday
    ```
    Output will indicate whether today is a bank holiday in the US (or another country if implemented later).</li>

</ol>


## Contributing
Everyone is welcome to contribute!

The idea is to create a CLI tool that can handle simple Google searches or repetitive tasks that we all do daily, right from the terminal. Here are some possible ideas for future features:

- Weather forecast
- Currency exchange rates
- News headlines
- Dictionary lookups
- More country-specific bank holiday checks
- Sports fixtures

If you want to add a new feature, simply fork the repository, implement your functionality, and submit a pull request!

## Future Goals
FastFind is a work in progress, and we envision it growing into a versatile tool for terminal-based quick searches and tasks. Any reasonable and simple functionality that can help save time by avoiding browser distractions is a candidate for this tool.

License
This project is open-source and available under the MIT License.

Happy coding, and let’s keep improving FastFind together! 😊