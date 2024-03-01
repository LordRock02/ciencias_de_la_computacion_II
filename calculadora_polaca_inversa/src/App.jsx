/* eslint-disable no-unused-vars */
import { useState } from 'react'
import './App.css'
import { CalcBtn } from './CalcBtn'

function App() {
  return (
    <div id='keys'>
      <CalcBtn sym='+'/>
      <CalcBtn sym='7'/>
      <CalcBtn sym='8'/>
      <CalcBtn sym='9'/>
      <CalcBtn sym='-'/>
      <CalcBtn sym='4'/>
      <CalcBtn sym='5'/>
      <CalcBtn sym='6'/>
      <CalcBtn sym='*'/>
      <CalcBtn sym='1'/>
      <CalcBtn sym='2'/>
      <CalcBtn sym='3'/>
      <CalcBtn sym='/'/>
      <CalcBtn sym='0'/>
      <CalcBtn sym='0'/>
      <CalcBtn sym='='/>
      <CalcBtn sym='C'/>
    </div>
  )
}

export default App
