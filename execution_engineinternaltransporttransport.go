package transport

import (
    "context"
    "log"
)

type TransportLayer struct {
    // TODO: Implement Flashbots, bloXroute, etc.
}

func NewTransportLayer() *TransportLayer {
    return &TransportLayer{}
}

func (tl *TransportLayer) SendTransaction(ctx context.Context, tx []byte) error {
    log.Println("Sending transaction...")
    // TODO: Implement private mempool submission
    return nil
}