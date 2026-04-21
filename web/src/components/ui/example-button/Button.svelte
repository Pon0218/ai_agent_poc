<script lang="ts">
	import { cva, type VariantProps } from 'class-variance-authority';
	import { cn } from '@/utils/cn';
	import { Button as BitsButton } from 'bits-ui';

	const buttonVariants = cva(
		'cursor-pointer rounded transition-opacity disabled:cursor-not-allowed disabled:opacity-40',
		{
			variants: {
				variant: {
					primary:
						'bg-s-background px-3 py-2 text-[14px] tracking-[0.52px] text-s-main hover:opacity-80',
					ghost: 'border border-s-background/18 px-3 py-2 text-[14px] tracking-[0.52px] text-s-sub-headline hover:opacity-70',
					secondary:
						'min-w-21 bg-s-card-background px-3 py-2 text-[12px] text-s-sub-headline hover:opacity-75'
				}
			},
			defaultVariants: {
				variant: 'primary'
			}
		}
	);

	type ButtonVariants = VariantProps<typeof buttonVariants>;

	let {
		variant = 'primary',
		class: className,
		...restProps
	}: ButtonVariants & BitsButton.RootProps = $props();
</script>

<BitsButton.Root class={cn(buttonVariants({ variant }), className)} {...restProps} />
