describe('Test Login', function(){
  beforeEach(function(){
    cy.log(Cypress.config("users").default.email)
    cy.login(Cypress.config("users").default.email, Cypress.config("users").default.password)
  })
  it('Check for form on /backend/projekte', function(){
    cy.visit('/backend/projekte/')
  
    cy.get('#datatable-filter-form').as('form')

    cy.get('@form').contains('#id_projekt_produkttypen', 'EnergieAudit')

    cy.get('#id_projekt_produkttypen').as('ProductTypeInput')//.select('EnergieAudit')
    cy.get('@ProductTypeInput')
      .select(['Startprodukte', 'EnergieAudit']).invoke('val')
      .should('deep.equal', ['10', '5'])

    cy.screenshot()

  })

})
