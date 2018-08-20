describe('The Home Page', function() {
  it('successfully loads', function() {
    cy.visit('/')
    cy.get('header.App-header h1').should('contain', 'My Product Store')
    cy.get('ul.product-list').find('li').should('have.length', 12)
  })
})