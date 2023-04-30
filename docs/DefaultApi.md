# swagger_client.DefaultApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_forgot_password_post**](DefaultApi.md#auth_forgot_password_post) | **POST** /auth/forgot-password | Envia um e-mail com um token exclusivo para redefinir a senha do usuário.
[**auth_login_post**](DefaultApi.md#auth_login_post) | **POST** /auth/login | Autentica o usuário e retorna um token de acesso.
[**auth_register_post**](DefaultApi.md#auth_register_post) | **POST** /auth/register | Cria uma nova conta de usuário no sistema.
[**auth_update_user_put**](DefaultApi.md#auth_update_user_put) | **PUT** /auth/update-user | Altera os dados de login do usuário autenticado.


# **auth_forgot_password_post**
> auth_forgot_password_post(email=email)

Envia um e-mail com um token exclusivo para redefinir a senha do usuário.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
email = swagger_client.ForgotPasswordRequest() # ForgotPasswordRequest | E-mail do usuário que deseja redefinir a senha. (optional)

try:
    # Envia um e-mail com um token exclusivo para redefinir a senha do usuário.
    api_instance.auth_forgot_password_post(email=email)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_forgot_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)| E-mail do usuário que deseja redefinir a senha. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> TokenResponse auth_login_post(credentials=credentials)

Autentica o usuário e retorna um token de acesso.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
credentials = swagger_client.LoginRequest() # LoginRequest | Credenciais do usuário. (optional)

try:
    # Autentica o usuário e retorna um token de acesso.
    api_response = api_instance.auth_login_post(credentials=credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**LoginRequest**](LoginRequest.md)| Credenciais do usuário. | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register_post**
> auth_register_post(user=user)

Cria uma nova conta de usuário no sistema.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user = swagger_client.RegisterRequest() # RegisterRequest | Informações do usuário a serem cadastradas. (optional)

try:
    # Cria uma nova conta de usuário no sistema.
    api_instance.auth_register_post(user=user)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**RegisterRequest**](RegisterRequest.md)| Informações do usuário a serem cadastradas. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_update_user_put**
> auth_update_user_put(authorization, update=update)

Altera os dados de login do usuário autenticado.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | Token de acesso do usuário.
update = swagger_client.UpdateUserRequest() # UpdateUserRequest | Dados a serem atualizados pelo usuário. (optional)

try:
    # Altera os dados de login do usuário autenticado.
    api_instance.auth_update_user_put(authorization, update=update)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_update_user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Token de acesso do usuário. | 
 **update** | [**UpdateUserRequest**](UpdateUserRequest.md)| Dados a serem atualizados pelo usuário. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

