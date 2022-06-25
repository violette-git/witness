





document.addEventListener('DOMContentLoaded', async function () {
    const payment = window.Square.payments(
        'sandbox-sq0idb-1fNSS5qWZD1aOeDxZN8dqw'
    )
});

const cashReq = payment.paymentRequest({
    countryCode: 'US',
    currencyCode: 'USD',
    total: {amount: '579', label: 'Total'},
})

const cashAppPay = await payment.cashAppPay(cashReq,{
    redirectURL: window.location.href,
    referenceId: `optional-reference-id`,
})

cashAppPay.addEventListener('onTokenization', ({ detail }) => {
    const { tokenResult } = detail;
    if (tokenResult.status === 'OK') {
        alert(tokenResult.token)
    }
})

const cashAppPayButton = document.getElementById('#pay-button')

await cashAppPay.attach('#pay-button')
