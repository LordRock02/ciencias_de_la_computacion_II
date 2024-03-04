/* eslint-disable react/prop-types */
export function Node({node, child1, child2}){
    return(
        <>
            <span>{node}</span>
            <div>{child1}</div>
            <div>{child2}</div>
        </>
    )
}
export function BinaryTree({stack}){
    const symbols ={
        '+' : 'operator',
        '-' : 'operator',
        '*' : 'operator',
        '/' : 'operator',
        '↑' : 'operator',
        '^' : 'operator'
    }
    let arr = stack
    let aux = []
    let sym = null
    while(arr.length>0){
        sym = arr.pop()
        if(symbols[sym]=='operator'){
            let a = aux.pop()
            let b = aux.pop()
            aux.push(<Node node={sym} child1={b} child2={a}></Node>)
        }else if(typeof parseFloat() == 'number'){
            aux.push(<Node node={sym}></Node>)
        }
    }
    if(aux.length>1){
        alert('ERRROR')
        document.getElementById('display').setAttribute('value','')
        return(<h1><strong>ERROR</strong></h1>)
    }
    return(aux.pop())
}