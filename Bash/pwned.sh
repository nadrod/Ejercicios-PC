!/bin/bash
#SCRIPT ELABORADO POR JAIRO SANTANA GARCIA, PABLO DE JESUS GARCIA MEDINA, JOSE PABLO PEREZ HERNANDEZ
#Modo de uso path relativo o absoluto del script y archivo txt como parametro
#EJEMPLO DE USO: ./pwned.sh correo.txt

read -s -p 'Ingrese tu api key del servicio Have I been Pwned?: ' key
echo -e "\n"

txt="$1"

function pwned(){

while IFS= read -r line
do
  echo -e "Verificando el correo: $line"
  url="https://haveibeenpwned.com/api/v3/breachedaccount/$line"

  curl -H "hibp-api-key:$key" -H "user-agent: Beyond the Frame" -sS "$url" -o verificacion.txt 2>/dev/null
  x=./verificacion.txt
  if [ -s "$x" ] 
  then
     echo -e "Sus datos han sido vulnerados en los siguientes lugares: \n"
     curl -H "hibp-api-key:$key" -H "user-agent: Beyond the Frame" -sS "$url" 2>/dev/null
     echo -e "\n"
  else
     echo -e "Enhorabuena sus datos no han sido vulnerados"
  fi
  echo -e "\n------------------------------------------------------------------------------\n" 
  sleep 5s #Es para evitar error 429 por demasiadas solicitudes en poco tiempo, eliminar o cambiar en caso necesario
done < $txt
}

pwned

 
