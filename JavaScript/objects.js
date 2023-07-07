function createObject(name, subs) {
    const myObject = {
      name: name,
      subscribers: subs,
      getStatus : function () {
        return `El canal de ${this.name} tiene ${this.subscribers} suscriptores`
      },
    
    };
    myObject.hash = myObject.name.length * subs;
return myObject;
}

const gaizka = createObject('Gaizka', 58992);
console.log(gaizka);
console.log(gaizka.getStatus());


