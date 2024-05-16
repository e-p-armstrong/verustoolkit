# Invoice Specification

The VerusPay Invoice specification, introduced in VerusPay v3, outlines a standardized format for creating, managing, and interpreting invoices across the Verus blockchain ecosystem and beyond. It is designed to be universally implementable across various programming languages, focusing primarily on the serialization and deserialization processes to ensure interoperability and consistency. VerusPay invoices provide a robust framework for blockchain invoice management, emphasizing interoperability, security, and ease of use. Their design facilitates a seamless payment experience across different blockchain ecosystems, making it a valuable tool for developers, merchants, and users within the Verus network and beyond.

## Core Components

The VerusPay Invoice construct is central to this specification, encapsulating all necessary information for a comprehensive invoice system, including:

- **System ID**: If the invoice is signed by a VerusID, this is the ID system it is signed on.
- **Signing ID**:  If the invoice is signed by a VerusID, this is the address of the VerusID that signed it.
- **Signature**:  If the invoice is signed by a VerusID, this is the signature.
- **Details**: Incorporates detailed transaction information through the VerusPay InvoiceDetails sub-component, covering aspects such as the payment amount, destination, and currency.
- **Version**: Manages the invoice format version, facilitating future updates and backward compatibility through version flags and checks.

### VerusPay InvoiceDetails

Embedded within the VerusPay Invoice, the VerusPay InvoiceDetails component provides specific transaction-related data:

- **Flags**: Configurable flag bits for invoice options.
- **Amount**: The payment amount specified in the invoice.
- **Destination**: Details about the payment destination, utilizing the [TransferDestination](/addresses/transfer-destination) construct for flexibility across different types of destinations.
- **Requested Currency ID**: The identifier for the currency in which the payment is requested.
- **Expiry Height**: Optionally specifies a Verus blockchain height after which the invoice is considered expired.
- **Max Estimated Slippage**: Defines the acceptable slippage for currency conversions, if applicable. Denoted as a satoshi representation of a percentage in decimal format (between 0 and 1).
- **Accepted Systems**: Lists blockchain systems or platforms accepted for payment other than VRSC/VRSCTEST.

#### Flags

- **VERUSPAY_INVALID (0)**: Indicates that the invoice is invalid. This default state can be used to signify that an invoice should not be processed.
- **VERUSPAY_VALID (1)**: Signifies that the invoice is valid and can be processed. This flag must be set for the invoice to be considered actionable.
- **VERUSPAY_ACCEPTS_CONVERSION (2)**: Specifies that the invoice accepts currency conversions. This allows payments in different currencies, with conversion to the invoice's requested currency. If an invoice accepts conversion, it requires a max estimated slippage value.
- **VERUSPAY_ACCEPTS_NON_VERUS_SYSTEMS (4)**: Indicates that payments from non-Verus blockchain systems are accepted. If this flag is set, specifying accepted systems is required.
- **VERUSPAY_EXPIRES (8)**: Determines that the invoice has an expiry condition. If set, the invoice must be paid before a specific Verus blockchain height is reached, and an expiry height must be set.
- **VERUSPAY_ACCEPTS_ANY_DESTINATION (16)**: Allows the invoice to accept payments to any destination. If set, the destination field in the invoice must be left blank.
- **VERUSPAY_ACCEPTS_ANY_AMOUNT (32)**: Indicates that the invoice can be paid with any amount. This is useful for donations or when the exact payment amount is not fixed. If set, the amount field in the invoice must be left blank.
- **VERUSPAY_EXCLUDES_VERUS_BLOCKCHAIN (64)**: If set, invoice cannot be paid on VRSC/VRSCTEST.
- **VERUSPAY_IS_TESTNET (128)**: Marks the invoice as only valid on VRSCTEST and/or testnet PBaaS blockchains, and establishes that all currencies/identities referenced within the invoice exist only on testnet.

## Serialization and Deserialization

![veruspay-invoice-bytes](/images/veruspay-invoice-bytes.svg)

The specification emphasizes a standardized approach to converting the VerusPay Invoice and VerusPay InvoiceDetails into a binary format (serialization) and back (deserialization) to enable efficient transmission and storage. This process ensures that invoices can be shared, processed, and stored across different systems and languages without loss of fidelity or meaning.

### Packaging into Deeplinks and QR Codes

To package a VerusPay Invoice into a deeplink or QR code readable by wallets like [Verus Mobile](https://github.com/VerusCoin/Verus-Mobile), the invoice must be serialized using the method described above, without its 20-byte [VDXF](/vdxf/) key included, and then its bytes formatted into a base64url string. Then, a deeplink URL can be created as follows: 

```[vrsc::applications.wallet VDXF ID]://x-callback-url/[veruspay.vrsc::invoice VDXF ID]/[VerusPay invoice bytes in base64url format]```

In practice, this creates URLs such as `i5jtwbp6zymeay9llnraglgjqgdrffsau4://x-callback-url/iEETy7La3FTN2Sd2hNRgepek5S8x8eeUeQ/AzABpJ-uxwACFAAtMxHDi_0hkJLSrvRJgEvos77-pu-eojVjXjKBJP80KdufnpG2Ti0`, which can then be packaged into a QR code and scanned by a VerusPay supporting wallet application, or linked to by an application or service to trigger an invoice request.