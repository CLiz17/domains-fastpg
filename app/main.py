from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
import datetime
from . import models, database, schemas

app = FastAPI()

@app.post("/domains", status_code=201)
def create_domain(domain: schemas.DomainCreate, db: Session = Depends(database.get_db)):
    try:
        domain_id = uuid.uuid4()        
        new_domain = models.Domain(
            domain_id=domain_id,
            domain_name=domain.domain_name,
            created_time=datetime.datetime.utcnow(), 
            https_enabled=https_enabled 
        )
        
        db.add(new_domain)
        db.commit()
        db.refresh(new_domain)
        
        return {"status": "OK"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create domain: {str(e)}"
        )

@app.get("/domains", response_model=list[schemas.DomainOut])
def read_domains(db: Session = Depends(database.get_db)):
    domains = db.query(models.Domain).all()
    return [
        {
            "domain_id": domain.domain_id,
            "domain_name": domain.domain_name,
            "created_time": domain.created_time,
            "https_enabled": domain.https_enabled
        }
        for domain in domains
    ]