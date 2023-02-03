<!DOCTYPE html>
<html>
<head>
  <title>Calculator with Gross and Net Buttons</title>
  <style>
    .calculator {
      background-color: pink;
      padding: 20px;
      border-radius: 10px;
      text-align: center;
    }
    input[type="button"] {
      background-color: #ff69b4;
      border: none;
      border-radius: 10px;
      color: white;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <form name="form1">
      <input type="text" name="answer" readonly>
      <br><br>
      <input type="button" value="1" onclick="form1.answer.value+='1'">
      <input type="button" value="2" onclick="form1.answer.value+='2'">
      <input type="button" value="3" onclick="form1.answer.value+='3'">
      <input type="button" value="+" onclick="form1.answer.value+='+'">
      <br>
      <input type="button" value="4" onclick="form1.answer.value+='4'">
      <input type="button" value="5" onclick="form1.answer.value+='5'">
      <input type="button" value="6" onclick="form1.answer.value+='6'">
      <input type="button" value="-" onclick="form1.answer.value+='-'">
      <br>
      <input type="button" value="7" onclick="form1.answer.value+='7'">
      <input type="button" value="8" onclick="form1.answer.value+='8'">
      <input type="button" value="9" onclick="form1.answer.value+='9'">
      <input type="button" value="*" onclick="form1.answer.value+='*'">
      <br>
      <input type="button" value="C" onclick="form1.answer.value=''">
      <input type="button" value="0" onclick="form1.answer.value+='0'">
      <input type="button" value="=" onclick="form1.answer.value=eval(form1.answer.value)">
      <input type="button" value="/" onclick="form1.answer.value+='/'">
      <br><br>
      <input type="button" value="Gross" onclick="form1.answer.value = Math.round(form1.answer.value*1.15 + 5)">
      <input type="button" value="Net" onclick="form1.answer.value = Math
