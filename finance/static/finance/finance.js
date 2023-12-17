document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  // document.querySelector('#account').addEventListener('click', load_account);
  document.querySelector('#history').addEventListener('click', load_history);
  document.querySelector('#trade').addEventListener('click', make_trade);

  // Execute Trade Submit
  document.querySelector('#trade-form').addEventListener('submit', execute_trade);

  // By default, load the account page
  // load_account();
});

function make_trade() {

  // Show trade view and hide other views
  // document.querySelector('#account-view').style.display = 'none';
  document.querySelector('#history-view').style.display = 'none';
  document.querySelector('#transaction-view').style.display = 'none';
  document.querySelector('#trade-view').style.display = 'block';

  // Clear out composition fields. 
  // Not Necessary.

}

function load_history() {
  
  // Show the trade history and hide other views
  // document.querySelector('#account-view').style.display = 'none';
  document.querySelector('#history-view').style.display = 'block';
  document.querySelector('#transaction-view').style.display = 'none';
  document.querySelector('#trade-view').style.display = 'none';


  // Set the page header
  document.querySelector('#history-view').innerHTML = `<h3>Transaction History</h3>`;

  // Make API Call to receive trade history from backend
  fetch('/trades/history')
  .then(response => response.json())
  .then(trades => {
      // Print trades
      console.log(trades);
  
      // ... do something else with trades ...

      //Loop through trades
      trades.forEach(trade => {
        
        console.log(trade);

        const displayTrade = document.createElement('div');
        displayTrade.className = 'list-group-item rounded my-3';
        displayTrade.innerHTML = `
          <h5> ${trade.stock} </strong></h5>
          <p><strong>Transaction:</strong> ${trade.transaction}
            <span>${trade.timestamp}</span>
          </p>
        `;
        

        // View Trade
        displayTrade.addEventListener('click', function() {
          view_trade(trade.id);
        });
        document.querySelector('#history-view').append(displayTrade);

      });
  });
}

// function load_account(){
//   return true
// }

function view_trade(id){

  // Make API Call to recieve trade information from backend
  fetch(`/trades/${id}`)
  .then(response => response.json())
  .then(trade => {
    // Print email
    console.log(trade);

    // ... do something else with email ...
    
    // Show the email and hide other views
    // document.querySelector('#account-view').style.display = 'none';
    document.querySelector('#history-view').style.display = 'none';
    document.querySelector('#transaction-view').style.display = 'block';
    document.querySelector('#trade-view').style.display = 'none';

    // Show the trade contents
    document.querySelector('#transaction-view').innerHTML = `
      <ul class="list-group list-group-flush border-bottom py-3 my-3">
        <li><strong>Trader:</strong> ${trade.trader}</li>
        <li><strong>Ticker:</strong> ${trade.stock}</li>
        <li><strong>Type:</strong> ${trade.transaction}</li>
        <li><strong>Quantity:</strong> ${trade.quantity}</li>
        <li><strong>Time:</strong> ${trade.timestamp}</li>
      </ul>
    `;
  });
}

function execute_trade(event){
  event.preventDefault();
  
  // Gather inputs from form inputs
  const type = document.querySelector('#trade-type').value;
  const ticker = document.querySelector('#trade-ticker').value;
  const quantity = document.querySelector('#trade-quantity').value;
  
  // API Call to fetch price data
  // fetch(`https://cloud.iexapis.com/stable/stock/${symbol}/quote?token=${api_key}`, {
  //   method: 'POST',
  //   body: JSON.stringify({  
  //     transaction: type,
  //     ticker: ticker,
  //     quantity: quantity,
  //     price: price
  //   })
  // })
  
  // const price = document.querySelector('#trade-price').value;

  // Make API Call to send trade information to backend
  fetch('/trades', {
    method: 'POST',
    body: JSON.stringify({  
      transaction: type,
      ticker: ticker,
      quantity: quantity
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      // Redirect to inbox
      // load_account();
  });
}