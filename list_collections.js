firestore.listCollections().then(collections => {
    for (let collection of collections) {
      console.log(`Found collection with id: ${collection.id}`);
    }
  });