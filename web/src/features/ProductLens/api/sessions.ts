import { z } from 'zod';
import { env } from '@/config/env';
import { anonymized_api } from '@/lib/api-client';

// ---------------------------------- API URL ----------------------------------------------------
export const url = `${env.API_URL}/sessions`;

// --------------------------------- 1. Zod Schema & TypeScript Types ------------------------------

export const InputSchema = z.object({
	product_name: z.string().min(1),
	website_url: z.string().url().min(1).nullable().optional(),
	product_description: z.string().nullable().optional()
});

export const OutputSchema = z.object({
	success: z.boolean(),
	data: z.object({
		session_id: z.string(),
		status: z.string(),
		message: z.string()
	}),
	error: z.string().nullable(),
	meta: z
		.object({
			message: z.string().nullable().optional()
		})
		.nullable()
});

export type InputType = z.infer<typeof InputSchema>;
export type OutputType = z.infer<typeof OutputSchema>;

// ---------------------------------- 2. Fetcher Function ------------------------------------------

export async function createSession(payload: InputType): Promise<OutputType> {
	const res = await anonymized_api.post(url, payload);
	return OutputSchema.parse(res);
}
