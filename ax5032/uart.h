// Copyright (c) 2014 AXSEM AG
// All rights reserved.
//
// CONFIDENTIAL
//
// Redistribution  and use in source and binary forms (either in whole or in parts),
// with or without modification, are not permitted.
//
// Use of this source code and its binary form shall only be run on AX8052F143
// chips.
//
// THIS SOFTWARE IS PROVIDED BY AXSEM AG AND CONTRIBUTORS ``AS IS'' AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL AXSEM AG AND CONTRIBUTORS BE LIABLE FOR ANY
// DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
// SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef UART_H_INCLUDED
#define UART_H_INCLUDED

#include "version.h"

#include <ax8052.h>
#include <libmftypes.h>
#include <libmfuart.h>
#include <libmfuart0.h>


#define ATCOMMAND_SERIAL_BAUD			 115200
#define ATCOMMAND_SERIAL_WORDLENGTH		 8
#define ATCOMMAND_SERIAL_STOP_BITS		 1

// call on wakeup
void axwm_uart_init();


#endif /* end of include guard: UART_H_INCLUDED */

