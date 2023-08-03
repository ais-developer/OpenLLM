import torch
import triton.language as tl
from _typeshed import Incomplete

from . import custom_autotune as custom_autotune

logger: Incomplete

def quant_matmul_248_kernel(a_ptr, b_ptr, c_ptr, scales_ptr, zeros_ptr, g_ptr, M, N, K, bits, maxq, stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn, stride_scales, stride_zeros, BLOCK_SIZE_M: tl.constexpr, BLOCK_SIZE_N: tl.constexpr, BLOCK_SIZE_K: tl.constexpr, GROUP_SIZE_M: tl.constexpr): ...
def transpose_quant_matmul_248_kernel(a_ptr, b_ptr, c_ptr, scales_ptr, zeros_ptr, g_ptr, M, N, K, bits, maxq, stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn, stride_scales, stride_zeros, BLOCK_SIZE_M: tl.constexpr, BLOCK_SIZE_N: tl.constexpr, BLOCK_SIZE_K: tl.constexpr, GROUP_SIZE_M: tl.constexpr): ...
def silu(x): ...
def quant_matmul_248(input, qweight, scales, qzeros, g_idx, bits, maxq): ...
def transpose_quant_matmul_248(input, qweight, scales, qzeros, g_idx, bits, maxq): ...

class QuantLinearFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input, qweight, scales, qzeros, g_idx, bits, maxq): ...
    @staticmethod
    def backward(ctx, grad_output): ...

def quant_matmul_inference_only_248(input, qweight, scales, qzeros, g_idx, bits, maxq): ...

class QuantLinearInferenceOnlyFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input, qweight, scales, qzeros, g_idx, bits, maxq): ...