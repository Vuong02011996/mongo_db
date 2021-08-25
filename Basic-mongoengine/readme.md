# Mongo engine basic
+ [Reference-mongoengine.org](https://docs.mongoengine.org/guide/document-instances.html#saving-and-deleting-documents)
+ [Reference](https://github.com/parisnakitakejser/video-tutorial-python-code/tree/master/mongoengine)

1. Connect
   The data basename can exit or not exit.
2. Insert new document.
   + Create class document: define field , datatype
   + Main: assign data to field and save().
   ```
   page = Page(title="Test Page")
   page.save()  # Performs an insert
   page.title = "My Page"
   page.save()  # Performs an atomic set on the title field.
   ```
    
3. Update document.
   + Static params field updater.
      + ob_document.update(field update)
   + Dynamic params field updater
      + create dictionary field need update
      + ob_document.update(**dictionary)
   ```
   ```
4. Working with index
   +
   Pending

5. Custom name collection and fields.
   Pending
   
6 Working with embedded document(sub-document in document)
   + Compare EmbeddedDocumentField with EmbeddedDocument ??
   + Create new sub-class EmbeddedDocument, define field, data type.
   + Assign sub-class EmbeddedDocument to main class document with EmbeddedDocumentField.
   ```
   ```

7. Insert document with embedded documents
   + assign data to field sub-class document.
   + assign ob_document by ob-sub-document.
   ```
   ```
8. Update the embedded documents.
   
   
# Field
+ EmbeddedDocumentField - Only valid values are subclasses of EmbeddedDocument
  
      