import React, {Component} from 'react'
import { Link } from 'react-router-dom'
import PropTypes from 'prop-types'
import sortBy from 'sort-by'
import escapeRegExp from 'escape-string-regexp'

class ListContacts extends Component {
  static propType = {
    contacts: PropTypes.array.isRequired,
    onDeleteContact: PropTypes.func.isRequired
  }
  state= {
    query: '',
  }
  updateQuery = (query) => {
    //Now when inputting to UI, it will remove whitespaces.
    this.setState({ query: query.trim() })
  }
  clearQuery = () => {
    this.setState({ query: '' })
  }
   render () {
     //instead of using this.props on each variable
     const {contacts, onDeleteContact } = this.props
     const { query } = this.state
     let showingContacts
     //Show alirie Truthy
     if (query) {
       const match = new RegExp(escapeRegExp(query),'i')
       showingContacts = contacts.filter((contact)=> match.test(contact.name))
     } else {
       showingContacts = contacts
     }
     // Sorting contacts based on specific key in array object.
    console.log(showingContacts)
      showingContacts.sort(sortBy('name'))
    return (

      <div className="list-contacts">
        <div className="list-contacts-top">
          <input
          className= 'search-contacts'
          type='text'
          placeholder="Search Contacts"
          //Setting the value to the state so we can control the input and ui elements
          //React controls the value not the dom waiting for event listeners
          value={ query }
          // When the value is changed on Dom update the UI element
          // If the showing contacts != contacts length then do the function
          onChange={(event) => this.updateQuery(event.target.value)}
          />
          <Link
            to="/create"
            //onClick={() => onNavigate()}
            //what it's doing
            className= "add-contact">
            Add Contact </Link>
        </div>
        {showingContacts.length !== contacts.length && (
         <div className='showing-contacts'>
           <span>Now showing {showingContacts.length} of {contacts.length} total</span>
           <button onClick={this.clearQuery}>Show all</button>
         </div>
       )}
       <ol className='contact-list'>
           {showingContacts.map((contact) => (
             <li key={contact.id} className='contact-list-item'>
               <div className='contact-avatar' style={{
                 backgroundImage: `url(${contact.avatarURL})`
               }}/>
               <div className='contact-details'>
                 <p>{contact.name}</p>
                 <p>{contact.email}</p>
               </div>
               <button onClick={() => onDeleteContact(contact)} className='contact-remove'>
                 Remove
               </button>
             </li>
           ))}
         </ol>
       </div>
  )
}
}

// onClick={()=> this.clearQuery()}



//Setting rules for the object types required by (Stateless function)m * now inside of class Component
//ListContacts.propTypes = {
//  contacts: PropTypes.array.isRequired,
  //onDeleteContact: PropTypes.func.isRequired
//}


export default ListContacts
