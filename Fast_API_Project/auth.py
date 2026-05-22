from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2AuthorizationCodeBearer
from jose import JWTError ,jwt
from fastapi import APIRouter

router=APIRouter(
    prefix='/auth',
    tags=['auth']
)