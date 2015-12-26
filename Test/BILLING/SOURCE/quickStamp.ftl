<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:stam="http://facturacion.finkok.com/stamp">
   <soapenv:Header/>
   <soapenv:Body>
      <stam:quick_stamp>
         <!--Optional:-->
         <stam:xml>${xmlBase64}</stam:xml>
         <!--Optional:-->
         <stam:username>${username}</stam:username>
         <!--Optional:-->
         <stam:password>${password}</stam:password>
      </stam:quick_stamp>
   </soapenv:Body>
</soapenv:Envelope>
