describe('Test Login', function(){
  beforeEach(function(){
    cy.log(Cypress.config("users").default.email)
    cy.login(Cypress.config("users").default.email, Cypress.config("users").default.password)
  })
  it('Check for form on /backend/projekte', function(){
    cy.visit('/backend/projekte/')
  
    cy.get('#datatable-filter-form').as('form')
    cy.screenshot()

  })

})


// describe('My First Test', function() {
//   it('Visits the Kitchen Sink', function() {
//     cy.visit('https://example.cypress.io')
//   })
// })