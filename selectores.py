#selectores.py
#Guarda los nombres de los selectores por pantalla
#Los retorna cuando se lo solicitan

#Defino la funcion que devuelvo los datos

def obtener_selectores_calculadora():
    
    selectores_calculadora = {
        "txt_numero1"    : "number1Field",
        "txt_numero2"    : "number2Field",
        "dp_operation"   : "selectOperationDropdown",
        "txt_resultado"  : "resultado",
        "bt_calculate"   : "calculateButton",
        "txt_answer"     : "numberAnswerField",
        "bt_clear"       : "clearButton"

    
    }

#Devuelve los datos de los nombres de los selectores del login

    return selectores_calculadora 


