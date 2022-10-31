MARKETPLACE CAR SERVER

===================Guildine=================
- Run server: uvicorn main:app
- Add dumb data from api
  + Add dubm brand data: baseUrl/brands/addAll
  + Add dubm car data: baseUrl/cars/addAll

===================Feature==================
  + Show list brand
  + View detail brand
  + Edit brand
  + Delete brand
  + Fetch list cars of brand
  + Filter brand
  + Filter car of brand

===================TechStack==================
Server: Python
  + Restful API integration: FastAPI
  + DB integration:
    - engine: SQLLite
    - mapping: ORM

