let display = document.getElementById('display');
let currentNumber = '';
let operator = '';
let previousNumber = '';

function appendNumber(number) {
    currentNumber += number;
    updateDisplay();
}

function operate(op) {
    if (currentNumber === '') return;
    if (previousNumber !== '') {
        calculate();
    }
    operator = op;
    previousNumber = currentNumber;
    currentNumber = '';
}

function calculate() {
    let result;
    switch (operator) {
        case '+':
            result = parseFloat(previousNumber) + parseFloat(currentNumber);
            break;
        case '-':
            result = parseFloat(previousNumber) - parseFloat(currentNumber);
            break;
        case '*':
            result = parseFloat(previousNumber) * parseFloat(currentNumber);
            break;
        case '/':
            result = parseFloat(previousNumber) / parseFloat(currentNumber);
            break;
        default:
            return;
    }
    currentNumber = result.toString();
    operator = '';
    previousNumber = '';
    updateDisplay();
}

function clearDisplay() {
    currentNumber = '';
    operator = '';
    previousNumber = '';
    updateDisplay();
}

function updateDisplay() {
    display.textContent = currentNumber;
}
