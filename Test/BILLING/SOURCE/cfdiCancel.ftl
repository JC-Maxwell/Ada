<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:can="http://facturacion.finkok.com/cancel" xmlns:apps="apps.services.soap.core.views" xmlns:can1="http://facturacion.finkok.com/cancellation">
   <soapenv:Header/>
   <soapenv:Body>
      <can:cancel>
         <!--Optional:-->
         <can:UUIDS>
            <!--Optional:-->
            <apps:uuids>
               <!--Zero or more repetitions:-->
               <can1:string>${uuid}</can1:string>
            </apps:uuids>
         </can:UUIDS>
         <!--Optional:-->
         <can:username>${username}</can:username>
         <!--Optional:-->
         <can:password>${password}</can:password>
         <!--Optional:-->
         <can:taxpayer_id>${identifier}</can:taxpayer_id>
         <!--Optional:-->
         <can:cer>${publicKeyPemBase64}</can:cer>
         <!--Optional:-->
         <can:key>${encriptedPrivateKeyPemBase64}</can:key>
         <!--Optional:-->
         <can:store_pending>?</can:store_pending>
      </can:cancel>
   </soapenv:Body>
</soapenv:Envelope>
