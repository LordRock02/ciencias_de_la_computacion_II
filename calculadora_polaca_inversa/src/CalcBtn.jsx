/* eslint-disable react/prop-types */
export function CalcBtn({sym}){
    const class_name = isNaN(sym)? 'operator-btn':''
    return(
        <button className={class_name}>{sym}</button>
    )
}