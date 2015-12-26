<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:reg="http://facturacion.finkok.com/registration">
   <soapenv:Header/>
   <soapenv:Body>
      <reg:add>
         <!--Optional:-->
         <reg:reseller_username>${username}</reg:reseller_username>
         <!--Optional:-->
         <reg:reseller_password>${password}</reg:reseller_password>
         <!--Optional:-->
         <reg:taxpayer_id>${newRFC}</reg:taxpayer_id>
         <!--Optional:-->
         <reg:coupon>?</reg:coupon>
         <!--Optional:-->
         <reg:added>?</reg:added>
      </reg:add>
   </soapenv:Body>
</soapenv:Envelope>
