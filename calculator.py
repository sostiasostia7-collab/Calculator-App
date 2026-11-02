<!DOCTYPE html>
<html lang="tl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Calculator</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --calc-bg: #1e293b;
            --btn-bg: #334155;
            --btn-hover: #475569;
            --op-bg: #f59e0b;
            --op-hover: #d97706;
            --action-bg: #475569;
            --action-hover: #64748b;
            --text-color: #f8fafc;
            --history-text: #94a3b8;
            --accent-color: #3b82f6;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            user-select: none;
        }

        body {
            background-color: var(--bg-color);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            display: flex;
            gap: 20px;
            max-width: 800px;
            width: 100%;
            flex-wrap: wrap;
            justify-content: center;
        }

        .calculator {
            background-color: var(--calc-bg);
            padding: 24px;
            border-radius: 24px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            width: 100%;
            max-width: 360px;
        }

        .display {
            background-color: #0f172a;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 20px;
            text-align: right;
            word-wrap: break-word;
            word-break: break-all;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.3);
        }

        .previous-operand {
            color: var(--history-text);
            font-size: 1rem;
            min-height: 1.2rem;
            transition: all 0.2s;
        }

        .current-operand {
            color: var(--text-color);
            font-size: 2.25rem;
            font-weight: 600;
            line-height: 1.2;
        }

        .buttons-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }

        button {
            border: none;
            outline: none;
            padding: 16px;
            font-size: 1.25rem;
            font-weight: 600;
            border-radius: 12px;
            cursor: pointer;
            color: var(--text-color);
            background-color: var(--btn-bg);
            transition: all 0.15s ease-in-out;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        button:hover {
            background-color: var(--btn-hover);
            transform: translateY(-2px);
        }

        button:active {
            transform: translateY(0);
        }

        button.operator {
            background-color: var(--op-bg);
            color: #ffffff;
        }

        button.operator:hover {
            background-color: var(--op-hover);
        }

        button.action {
            background-color: var(--action-bg);
        }

        button.action:hover {
            background-color: var(--action-hover);
        }

        button.span-two {
            grid-column: span 2;
        }

        button.equals {
            background-color: var(--accent-color);
        }

        button.equals:hover {
            background-color: #2563eb;
        }

        /* History Panel */
        .history-panel {
            background-color: var(--calc-bg);
            padding: 24px;
            border-radius: 24px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
            width: 100%;
            max-width: 300px;
            display: flex;
            flex-direction: column;
            max-height: 480px;
        }

        .history-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            color: var(--text-color);
        }

        .history-list {
            overflow-y: auto;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .history-item {
            background-color: rgba(15, 23, 42, 0.5);
            padding: 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s;
        }

        .history-item:hover {
            background-color: rgba(15, 23, 42, 0.9);
        }

        .history-item .exp {
            color: var(--history-text);
            font-size: 0.85rem;
            text-align: right;
        }

        .history-item .res {
            color: var(--accent-color);
            font-size: 1.1rem;
            font-weight: bold;
            text-align: right;
        }

        .clear-history-btn {
            background: transparent;
            color: #ef4444;
            font-size: 0.85rem;
            padding: 4px 8px;
            box-shadow: none;
        }

        .clear-history-btn:hover {
            background: rgba(239, 68, 68, 0.1);
            transform: none;
        }

        @media (max-width: 680px) {
            .history-panel {
                max-width: 360px;
                max-height: 250px;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Main Calculator -->
        <div class="calculator">
            <div class="display">
                <div class="previous-operand" id="previous-operand"></div>
                <div class="current-operand" id="current-operand">0</div>
            </div>
            
            <div class="buttons-grid">
                <button class="action" onclick="clearAll()">AC</button>
                <button class="action" onclick="deleteDigit()">⌫</button>
                <button class="action" onclick="appendOperator('%')">%</button>
                <button class="operator" onclick="appendOperator('÷')">÷</button>

                <button onclick="appendNumber('7')">7</button>
                <button onclick="appendNumber('8')">8</button>
                <button onclick="appendNumber('9')">9</button>
                <button class="operator" onclick="appendOperator('×')">×</button>

                <button onclick="appendNumber('4')">4</button>
                <button onclick="appendNumber('5')">5</button>
                <button onclick="appendNumber('6')">6</button>
                <button class="operator" onclick="appendOperator('-')">-</button>

                <button onclick="appendNumber('1')">1</button>
                <button onclick="appendNumber('2')">2</button>
                <button onclick="appendNumber('3')">3</button>
                <button class="operator" onclick="appendOperator('+')">+</button>

                <button onclick="appendNumber('0')">0</button>
                <button onclick="appendNumber('.')">.</button>
                <button class="span-two equals" onclick="compute()">=</button>
            </div>
        </div>

        <!-- History Side Panel -->
        <div class="history-panel">
            <div class="history-header">
                <h3>History</h3>
                <button class="clear-history-btn" onclick="clearHistory()">Clear</button>
            </div>
            <div class="history-list" id="history-list">
                <!-- History items will be inserted here -->
            </div>
        </div>
    </div>

    <script>
        let currentOperand = '0';
        let previousOperand = '';
        let operation = undefined;
        let shouldResetScreen = false;
        let history = [];

        const currentOperandText = document.getElementById('current-operand');
        const previousOperandText = document.getElementById('previous-operand');
        const historyList = document.getElementById('history-list');

        function updateDisplay() {
            currentOperandText.innerText = formatNumber(currentOperand);
            if (operation != null) {
                previousOperandText.innerText = `${formatNumber(previousOperand)} ${operation}`;
            } else {
                previousOperandText.innerText = '';
            }
        }

        function formatNumber(number) {
            if (number === '' || number === undefined) return '';
            if (number === 'Error') return 'Error';
            
            const stringNumber = number.toString();
            const integerDigits = parseFloat(stringNumber.split('.')[0]);
            const decimalDigits = stringNumber.split('.')[1];
            let integerDisplay;
            
            if (isNaN(integerDigits)) {
                integerDisplay = '';
            } else {
                integerDisplay = integerDigits.toLocaleString('en', { maximumFractionDigits: 0 });
            }

            if (decimalDigits != null) {
                return `${integerDisplay}.${decimalDigits}`;
            } else {
                return integerDisplay;
            }
        }

        function appendNumber(number) {
            if (currentOperand === '0' || shouldResetScreen) {
                resetOperand();
            }
            if (number === '.' && currentOperand.includes('.')) return;
            currentOperand = currentOperand.toString() + number.toString();
            updateDisplay();
        }

        function resetOperand() {
            currentOperand = '';
            shouldResetScreen = false;
        }

        function appendOperator(op) {
            if (currentOperand === 'Error') return;
            if (operation !== undefined && !shouldResetScreen) {
                compute();
            }
            operation = op;
            previousOperand = currentOperand;
            shouldResetScreen = true;
            updateDisplay();
        }

        function clearAll() {
            currentOperand = '0';
            previousOperand = '';
            operation = undefined;
            shouldResetScreen = false;
            updateDisplay();
        }

        function deleteDigit() {
            if (shouldResetScreen || currentOperand === 'Error') return;
            if (currentOperand.length === 1) {
                currentOperand = '0';
            } else {
                currentOperand = currentOperand.slice(0, -1);
            }
            updateDisplay();
        }

        function compute() {
            let computation;
            const prev = parseFloat(previousOperand);
            const current = parseFloat(currentOperand);

            if (isNaN(prev) || isNaN(current)) return;

            switch (operation) {
                case '+':
                    computation = prev + current;
                    break;
                case '-':
                    computation = prev - current;
                    break;
                case '×':
                    computation = prev * current;
                    break;
                case '÷':
                    if (current === 0) {
                        alert("Hindi pwedeng mag-divide sa zero!");
                        clearAll();
                        return;
                    }
                    computation = prev / current;
                    break;
                case '%':
                    computation = (prev * current) / 100;
                    break;
                default:
                    return;
            }

            // Save to history
            const expressionStr = `${formatNumber(prev)} ${operation} ${formatNumber(current)}`;
            const resultStr = computation.toString();
            
            addHistory(expressionStr, formatNumber(resultStr));

            currentOperand = computation.toString();
            operation = undefined;
            previousOperand = '';
            shouldResetScreen = true;
            updateDisplay();
        }

        function addHistory(expression, result) {
            history.unshift({ expression, result });
            renderHistory();
        }

        function renderHistory() {
            historyList.innerHTML = '';
            history.forEach(item => {
                const historyDiv = document.createElement('div');
                historyDiv.classList.add('history-item');
                historyDiv.innerHTML = `
                    <div class="exp">${item.expression} =</div>
                    <div class="res">${item.result}</div>
                `;
                historyList.appendChild(historyDiv);
            });
        }

        function clearHistory() {
            history = [];
            renderHistory();
        }

        // Keyboard Support
        window.addEventListener('keydown', e => {
            if ((e.key >= '0' && e.key <= '9') || e.key === '.') {
                appendNumber(e.key);
            }
            if (e.key === '+') appendOperator('+');
            if (e.key === '-') appendOperator('-');
            if (e.key === '*') appendOperator('×');
            if (e.key === '/') {
                e.preventDefault();
                appendOperator('÷');
            }
            if (e.key === '%') appendOperator('%');
            if (e.key === 'Enter' || e.key === '=') {
                e.preventDefault();
                compute();
            }
            if (e.key === 'Backspace') deleteDigit();
            if (e.key === 'Escape') clearAll();
        });
    </script>
</body>
</html>

