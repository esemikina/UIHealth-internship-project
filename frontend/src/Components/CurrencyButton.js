import React, { useState } from 'react';
import styles from './CurrencyButton.module.css';


/* 
:currency:
  the current chosen currency
:type:
  string
:changeCurrency:
  function that change currency value on parent
:type:
  function
*/
function CurrencyButton ({currency,changeCurrency}) {
  // ToDo 10.1
      return (
      <div className={styles.buttonContainer}>
        <button
          onClick={() => changeCurrency('USD')}
          className={currency === 'USD' ? styles.currencyButtonActive : styles.currencyButtonDefault}
        >
          USD
        </button>
        <button
          onClick={() => changeCurrency('EUR')}
          className={currency === 'EUR' ? styles.currencyButtonActive : styles.currencyButtonDefault}
        >
          EUR
        </button>
      </div>
    );
  }



export default CurrencyButton;
