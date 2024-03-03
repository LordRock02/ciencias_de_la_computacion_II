export function evaluate(inicialInput){
    const symbols ={
        '+' : 'operator',
        '-' : 'operator',
        '*' : 'operator',
        '/' : 'operator',
        '↑' : 'operator',
        '^' : 'operator'
    }
    
    let inputStack = inicialInput.split(' ')
    let auxStack = []
    var operator=null
    var num1=null
    var num2=null
    var ans = 0

    //alert('input (initial): '+inputStack)

    while(inputStack.length>0){
        var res
        let sym = inputStack.pop()
        if(symbols[sym]=='operator'){
            operator = sym
            num1 = null
            num2 = null
        }else if(num1==null){
            num1 = parseFloat(sym)
        }else if(num2==null){
            num2 = parseFloat(sym)
        }
        auxStack.push(sym)

        if(operator != null && num1 != null && num2 != null){
            res = 0
            switch (operator){
                case '+':
                    res = num2 + num1
                    break
                case '-':
                    res = num2 - num1
                    break
                case '*':
                    res = num2 * num1
                    break
                case '/':
                    res = num2 / num1
                    break
                case '↑':
                    res = num2 ** num1
                    break
                case '^':
                    res = num2 ** num1
                    break
            }
            auxStack.pop()
            auxStack.pop()
            auxStack.pop()
            inputStack.push(res)
            operator=null
            num1=null
            num2=null
            while(auxStack.length > 0){
                inputStack.push(auxStack.pop())
            }
        }
        //alert(inputStack)
        if(inputStack.length == 1 && auxStack.length==0){
            ans = res
        }
    }
    return ans
}